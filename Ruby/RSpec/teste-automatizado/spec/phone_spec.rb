require 'phone'

RSpec.describe Phone do

  subject(:phone) { described_class.new(number) }

  describe '#valid_number?' do

    context 'when number is valid' do
      context 'when number contains only numbers' do
        let(:number) { '1234' }
  
        it 'returns true' do
          expect(phone.valid_number?).to eq(true)
        end
      end

      context 'when number contains numbers with spaces between them' do
        let(:number) { '123 456' }
  
        it 'returns true' do
          expect(phone.valid_number?).to eq(true)
        end
      end

    end

    context 'when number is empty' do
      let(:number) { '' }

      it 'returns false' do
        expect(phone.valid_number?).to eq(false)
      end
    end

    context 'when number is not valid' do
      context 'when number contains letters' do
        let(:number) { 'abcd' }
  
        it 'returns false' do
          expect(phone.valid_number?).to eq(false)
        end
      end

    end
  end
end